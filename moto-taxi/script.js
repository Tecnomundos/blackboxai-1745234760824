// Map initialization
let map;
let autocompletePickup;
let autocompleteDestination;
let directionsService;
let directionsRenderer;

function initMap() {
    // Initialize the map centered on Brazil
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -15.7801, lng: -47.9292 },
        zoom: 5,
        styles: [
            {
                featureType: "poi",
                elementType: "labels",
                stylers: [{ visibility: "off" }]
            }
        ]
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        map: map,
        suppressMarkers: true
    });

    // Initialize autocomplete for pickup and destination inputs
    autocompletePickup = new google.maps.places.Autocomplete(
        document.getElementById('pickup'),
        { types: ['address'], componentRestrictions: { country: 'BR' } }
    );

    autocompleteDestination = new google.maps.places.Autocomplete(
        document.getElementById('destination'),
        { types: ['address'], componentRestrictions: { country: 'BR' } }
    );

    // Add listeners for place selection
    autocompletePickup.addListener('place_changed', calculateRoute);
    autocompleteDestination.addListener('place_changed', calculateRoute);
}

function calculateRoute() {
    const pickup = document.getElementById('pickup').value;
    const destination = document.getElementById('destination').value;

    if (!pickup || !destination) return;

    const request = {
        origin: pickup,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING
    };

    directionsService.route(request, (result, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsRenderer.setDirections(result);
            
            // Calculate and display estimated price
            const distance = result.routes[0].legs[0].distance.value / 1000; // Convert to km
            const estimatedPrice = calculatePrice(distance);
            document.getElementById('estimatedPrice').textContent = 
                `R$ ${estimatedPrice.toFixed(2).replace('.', ',')}`;
        }
    });
}

function calculatePrice(distance) {
    const basePrice = 5.00; // Base fare
    const pricePerKm = 2.50; // Price per kilometer
    return basePrice + (distance * pricePerKm);
}

// Modal handling
document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
    const closeButtons = document.querySelectorAll('.closeModal');

    function openModal(modal) {
        modal.classList.remove('hidden');
        modal.classList.add('modal-enter');
    }

    function closeModal(modal) {
        modal.classList.add('modal-exit');
        setTimeout(() => {
            modal.classList.add('hidden');
            modal.classList.remove('modal-exit');
        }, 300);
    }

    loginBtn.addEventListener('click', () => openModal(loginModal));
    registerBtn.addEventListener('click', () => openModal(registerModal));

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('#loginModal, #registerModal');
            closeModal(modal);
        });
    });

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target === loginModal || e.target === registerModal) {
            closeModal(e.target);
        }
    });
});

// Ride request handling
document.getElementById('requestRide').addEventListener('click', async () => {
    const pickup = document.getElementById('pickup').value;
    const destination = document.getElementById('destination').value;
    
    if (!pickup || !destination) {
        alert('Por favor, preencha os locais de partida e destino.');
        return;
    }

    try {
        const response = await fetch('/api/request-ride', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                pickup,
                destination,
                estimated_price: parseFloat(document.getElementById('estimatedPrice').textContent.replace('R$ ', '').replace(',', '.'))
            })
        });

        if (!response.ok) {
            throw new Error('Erro ao solicitar corrida');
        }

        const data = await response.json();
        alert('Procurando mototaxistas próximos...');
        
        // Aqui você pode adicionar lógica para acompanhar o status da corrida
        // Por exemplo, iniciar um polling para verificar se um motorista aceitou

    } catch (error) {
        alert('Erro ao solicitar corrida. Por favor, tente novamente.');
        console.error('Error:', error);
    }
});

// Initialize map when the script loads
window.initMap = initMap;
