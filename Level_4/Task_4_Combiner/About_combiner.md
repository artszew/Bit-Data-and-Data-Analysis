Kiedy używać combinera:
Gdy operacja agreguje dane (np. sum, count, max, min)

Gdy funkcja redukująca jest łączalna (associative) i przemienna (commutative)
(czyli kolejność i grupowanie danych nie wpływają na wynik)

Gdy masz dużo powtarzających się kluczy — np. Polska 1, Polska 1, Polska 1

Gdy chcesz zmniejszyć ilość przesyłanych danych między mapperem a reducerem
Kiedy nie używać combinera:
Gdy obliczasz średnią, medianę, percentyle bez odpowiedniego formatu (suma, licznik)

Gdy operacja zależy od kolejności danych (np. first, last, sort)

Gdy dane są unikalne (np. user_id, transaction_id) — brak zysku

Gdy funkcja redukująca jest niemonotoniczna lub niedeterministyczna (np. używa random, czas, globalne zmienne)

Gdy nie możesz zagwarantować, że częściowe wyniki dadzą ten sam efekt po ponownym zredukowaniu

Używaj combinera, gdy możesz spokojnie zsumować dane lokalnie, a wynik tego sumowania można zsumować jeszcze raz — bez zmiany wyniku końcowego.

