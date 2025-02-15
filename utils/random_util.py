from faker import Faker

fake = Faker()


def generate_fake_text():
    """Генерирует случайный текст с использованием Faker."""
    return fake.text(max_nb_chars=10)
