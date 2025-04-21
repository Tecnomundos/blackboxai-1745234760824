"""
Wisdom Engine Module - Integrates ancient knowledge with modern transportation
"""
from datetime import datetime
import math

class LunarPhaseAnalyzer:
    """Analyzes lunar phases and their influence on journey planning"""
    
    LUNAR_PHASES = {
        'new_moon': {
            'characteristics': 'Beginnings, fresh starts, ideal for new journeys',
            'mental_state': 'Contemplative, ready for new experiences',
            'guidance': 'Best time for planning new routes and destinations'
        },
        'waxing_crescent': {
            'characteristics': 'Growth, building momentum, increasing energy',
            'mental_state': 'Enthusiastic, forward-looking',
            'guidance': 'Ideal for short distance travels and exploration'
        },
        'first_quarter': {
            'characteristics': 'Action, decision-making, overcoming challenges',
            'mental_state': 'Focused, determined',
            'guidance': 'Perfect for business-related travel and important meetings'
        },
        'waxing_gibbous': {
            'characteristics': 'Refinement, attention to detail, preparation',
            'mental_state': 'Detail-oriented, analytical',
            'guidance': 'Good for precise planning and scheduled rides'
        },
        'full_moon': {
            'characteristics': 'Culmination, clarity, maximum energy',
            'mental_state': 'Energetic, intuitive',
            'guidance': 'Optimal for long journeys and important travel'
        },
        'waning_gibbous': {
            'characteristics': 'Gratitude, sharing, teaching',
            'mental_state': 'Reflective, sharing wisdom',
            'guidance': 'Ideal for group travels and shared rides'
        },
        'last_quarter': {
            'characteristics': 'Release, letting go, completion',
            'mental_state': 'Contemplative, releasing',
            'guidance': 'Good for completing ongoing journeys'
        },
        'waning_crescent': {
            'characteristics': 'Rest, recovery, preparation',
            'mental_state': 'Restful, introspective',
            'guidance': 'Best for essential travel only, focus on rest'
        }
    }

    @staticmethod
    def calculate_lunar_phase(date=None):
        """Calculate current lunar phase based on date"""
        if date is None:
            date = datetime.now()
        
        # Simplified lunar phase calculation
        lunar_month = 29.53  # days
        reference_new_moon = datetime(2000, 1, 6)  # Known new moon date
        days_since_reference = (date - reference_new_moon).days
        phase = (days_since_reference % lunar_month) / lunar_month

        # Return appropriate phase based on calculation
        if 0 <= phase < 0.125:
            return 'new_moon'
        elif 0.125 <= phase < 0.25:
            return 'waxing_crescent'
        elif 0.25 <= phase < 0.375:
            return 'first_quarter'
        elif 0.375 <= phase < 0.5:
            return 'waxing_gibbous'
        elif 0.5 <= phase < 0.625:
            return 'full_moon'
        elif 0.625 <= phase < 0.75:
            return 'waning_gibbous'
        elif 0.75 <= phase < 0.875:
            return 'last_quarter'
        else:
            return 'waning_crescent'

class WisdomGuide:
    """Integrates ancient wisdom into journey planning"""
    
    WISDOM_PRINCIPLES = {
        'masonic': {
            'principles': ['Brotherhood', 'Truth', 'Charity'],
            'application': 'Foster community support in transportation'
        },
        'templar': {
            'principles': ['Protection', 'Service', 'Honor'],
            'application': 'Ensure safety and reliability in travel'
        },
        'buddhist': {
            'principles': ['Mindfulness', 'Compassion', 'Right Action'],
            'application': 'Practice mindful and considerate journey planning'
        },
        'vedic': {
            'principles': ['Dharma', 'Karma', 'Balance'],
            'application': 'Align travel with natural rhythms and purpose'
        }
    }

    @staticmethod
    def get_journey_guidance(origin, destination, lunar_phase):
        """Provide wisdom-based guidance for journey"""
        phase_info = LunarPhaseAnalyzer.LUNAR_PHASES[lunar_phase]
        
        guidance = {
            'mental_preparation': phase_info['mental_state'],
            'journey_characteristics': phase_info['characteristics'],
            'recommended_approach': phase_info['guidance'],
            'wisdom_integration': {
                'masonic': 'Focus on building connections during travel',
                'templar': 'Maintain vigilance and protect fellow travelers',
                'buddhist': 'Practice mindfulness throughout the journey',
                'vedic': 'Align travel time with natural rhythms'
            }
        }
        
        return guidance

class JourneyOptimizer:
    """Optimizes journey based on wisdom principles and lunar phases"""
    
    def __init__(self):
        self.lunar_analyzer = LunarPhaseAnalyzer()
        self.wisdom_guide = WisdomGuide()

    def optimize_journey(self, origin, destination, time=None):
        """
        Optimize journey based on lunar phase and wisdom principles
        """
        if time is None:
            time = datetime.now()
            
        lunar_phase = self.lunar_analyzer.calculate_lunar_phase(time)
        guidance = self.wisdom_guide.get_journey_guidance(origin, destination, lunar_phase)
        
        return {
            'lunar_phase': lunar_phase,
            'guidance': guidance,
            'optimal_time': self._suggest_optimal_time(lunar_phase),
            'journey_recommendations': self._get_recommendations(lunar_phase)
        }

    def _suggest_optimal_time(self, lunar_phase):
        """Suggest optimal time for journey based on lunar phase"""
        # Implementation would consider lunar phase and traditional wisdom
        optimal_times = {
            'new_moon': 'Dawn',
            'waxing_crescent': 'Morning',
            'first_quarter': 'Noon',
            'waxing_gibbous': 'Afternoon',
            'full_moon': 'Dusk',
            'waning_gibbous': 'Evening',
            'last_quarter': 'Night',
            'waning_crescent': 'Late night'
        }
        return optimal_times.get(lunar_phase, 'Any time')

    def _get_recommendations(self, lunar_phase):
        """Get specific recommendations based on lunar phase"""
        phase_info = LunarPhaseAnalyzer.LUNAR_PHASES[lunar_phase]
        return {
            'mental_preparation': f"Maintain a {phase_info['mental_state']} mindset",
            'journey_timing': f"Consider the {phase_info['characteristics']}",
            'travel_advice': phase_info['guidance']
        }
