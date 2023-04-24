# Pytest - Decorators
## Fonksiyonun davranışı değiştirmeye yararlar. Başlarken "@" ile başlar ve kodun anlaşabilirliğini ve hızını artırır.
### Temel Decorator
- parametrize
- timeout
- usefixtures
- filterwarnings
- skip

### Decorator Kullanımı
- @pytest.mark.parametrize: Birden fazla parametre ile test edilmesi sağlanır.
import pytest
<pre>
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
</pre>