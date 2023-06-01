# from django.test import TestCase
# from django.urls import reverse
# from restaurant.models import Menu

# class MenuViewTest(TestCase):
#     def setup(self):
#         Menu.objects.create(Title='Menu 1', Price=10, Inventory=5)
#         Menu.objects.create(Title='Menu 2', Price=20, Inventory=3)
#         Menu.objects.create(Title='Menu 3', Price=30, Inventory=7)

#     def test_getall(self):
#         url = reverse('menu-list')
#         response = self.client.get(url)
#         menus = Menu.objects.all()
#         serialized_data = [
#             {"id": menu.id, "Title": menu.Title, "Price": menu.Price, "Inventory": menu.Inventory}
#             for menu in menus
#         ]
#         self.assertEqual(response.data, serialized_data)
