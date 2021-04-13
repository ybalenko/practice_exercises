""" 
Создайте класс Editor, который содержит методы view_document и edit_document. 
Пусть метод edit_document выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии. 
Создайте подкласс ProEditor, в котором данный метод будет переопределён. 
Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor. 
Вызовите методы просмотра и редактирования документов.
 """


class Editor():
    def __init__(self, doc: str):
        self.doc = doc

    def view_document(self):
        print(self.doc)

    def edit_document(self):
        print("This feature is not available for free")


class EditorPro(Editor):

    def edit_document(self):
        new_doc_input = input("Enter new document here: ")
        self.doc = new_doc_input


if __name__ == '__main__':

    keys = ['12345', '67890']
    key_input = input("Please enter key: ")

    editor = None
    doc = "This is my document"
    if key_input in keys:
        editor = EditorPro(doc)
    else:
        editor = Editor(doc)

    editor.view_document()
    editor.edit_document()
