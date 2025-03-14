from django.test import TestCase
from .models import Lead

class LeadModelTestCase(TestCase):
    def setUp(self):
        self.lead = Lead.objects.create(
            name="Test Lead",
            email="test@example.com",
            phone="1234567890",
            industry="IT",
            score=80,
            priority="High"
        )

    def test_lead_creation(self):
        self.assertEqual(self.lead.name, "Test Lead")
        self.assertEqual(self.lead.email, "test@example.com")
        self.assertEqual(self.lead.priority, "High")

    def test_priority_choices(self):
        self.assertIn(self.lead.priority, [choice[0] for choice in Lead.PRIORITY_CHOICES])
