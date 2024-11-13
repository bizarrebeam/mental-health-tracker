from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

class mainTest(TestCase):
    # cek apakah path url utama '' bisa diakses
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    # cek apakah template yang digunakan adalah main.html
    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    # cek halaman yang tidak ada, beneran return 404 (bukan err response yang lain)
    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    # cek logic apakah mood pengguna bisa dikatakan kuat
    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="LUMAYAN SENANG",
          time = now,
          feelings = "senang sih, cuman tadi baju aku basah kena hujan :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)