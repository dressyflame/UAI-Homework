from console_file_manager import prog_author
from account import print_history, purchase

def test_prog_author():
    assert prog_author() == 'Создатель программы - Коданев Никита'

def test_print_history():
    #нет истории покупок
    assert print_history([]) == 'Вы еще не совершили ни одной покупки.'
    #есть какие то покупки
    assert print_history([('товар', '100')]) == 'название - сумма\nтовар - 100'
    assert print_history([('товар', '100'), ('другое','15')]) == 'название - сумма\nтовар - 100\nдругое - 15'

def test_purchase():
    #стоимость товара меньше чем депозит
    assert purchase('товар', 1, 10) == (1, ('товар', '1'))
    #стоимость товара больше чем депозит
    assert purchase('товар', 10, 1) == "Это слишком дорого, у вас недостаточно средств!"