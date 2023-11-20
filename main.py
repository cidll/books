from database import Database


database = Database()



def main():
	choice = input("1. Добавить книгу\n2. Просмотреть все книги\n3. Выйти\n--> ")

	if choice == "1":
		create()

	elif choice == "2":
		books()

	elif choice == "3":
		exit()

	else:
		print("Неверный выбор. Попробуйте снова.")
		main()



def books():
	print("\nВыберите книгу: \n")

	for i in database.get():
		print(f"ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}")

	q = input("\nДля просмотра информации о книге введите её название или автора: \nДля выхода введите 0\n-->")

	if q == "0":
		main()

	else:
		search(q)



def search(q):
	books = database.search(q)
	print(len(books))

	for i in books:
		print(f"ID: {i[0]}, Название: {i[1]}, Автор: {i[2]}, Описание: {i[3]} \n")

	choice = input("0. Назад \n1. Удалить книгу")

	if choice == "0":
		main()

	elif choice == "1":
		delete()

	else:
		main()



def delete():
	book = input("Введите ID книги для удаления: ")

	database.delete(book)
	print("Книга удалена")

	main()



def create():
	title = input("Введите заголовок книги: ")
	autor = input("Введите имя автора книги: ")
	genre = input("Введите жанр книги: ")
	description = input("Введите описание книги: ")

	database.add(title, autor, description, genre)
	print("Книга создана.")

	main()


main()
