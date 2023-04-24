# Pytest - Decorators
### Fonksiyonun davranışı değiştirmeye yararlar. Başlarken "@" ile başlar ve kodun anlaşabilirliğini ve hızını artırır.
#### Temel Decorator
- parametrize
- timeout
- usefixtures
- filterwarnings
- skip
- xfail

#### Decorator Kullanımı
- @pytest.mark.parametrize: Birden fazla parametre ile test edilmesi sağlanır.
<pre>
import pytest
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
</pre>

- @pytest.mark.timeout: Bir testin belirli bir sürede yapılması aksi halde başarısız sonuç vermesini sağlar.
<pre>
@pytest.mark.timeout(60)
def test_foo():
    pass
</pre>

- @pytest.usefixtures: Bir veritabanı veya kaynak ataması yapılır.
<pre>
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
</pre>

- @pytest.marks.filterwarnings: Uyarı filtreleri eklenir.

- @pytest.mark.skip: Bir testin atlanması sağlanır.

- @pytest.mark.xfail: Bir koşula bağlı başarısız test sonucu üretir.
