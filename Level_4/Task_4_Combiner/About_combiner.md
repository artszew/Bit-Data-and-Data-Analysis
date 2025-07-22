______
[EN]

### When to use a combiner:
- When the operation aggregates data (e.g., sum, count, max, min),
- When the reducer function is associative and commutative (meaning the order and grouping of data do not affect the result),
- When you have many duplicate keys — e.g., Poland 1, Poland 1, Poland 1,
- When you want to reduce the amount of data transferred between the mapper and the reducer.

### When not to use a combiner:
- When you calculate the mean, median, or percentile without the appropriate format (sum, count),
- When the operation depends on the order of the data (e.g., first, last, sort),
- When the data is unique (e.g., user_id, transaction_id) — no gain,
- When the reducer function is non-monotonic or non-deterministic (e.g., uses random, time, global variables),
- When you cannot guarantee that partial results will produce the same result after being reduced again.

### Use a combiner when you can safely sum the data locally, and the result of that sum can be summed again without changing the final result.

______
[PL]

### Kiedy używać combinera:
- Gdy operacja agreguje dane (np. sum, count, max, min),
- Gdy funkcja redukująca jest łączalna (associative) i przemienna (commutative) (czyli kolejność i grupowanie danych nie wpływają na wynik),
- Gdy masz dużo powtarzających się kluczy — np. Polska 1, Polska 1, Polska 1,
- Gdy chcesz zmniejszyć ilość przesyłanych danych między mapperem a reducerem.

### Kiedy nie używać combinera:
- Gdy obliczasz średnią, medianę, percentyle bez odpowiedniego formatu (suma, licznik),
- Gdy operacja zależy od kolejności danych (np. first, last, sort),
- Gdy dane są unikalne (np. user_id, transaction_id) — brak zysku,
- Gdy funkcja redukująca jest niemonotoniczna lub niedeterministyczna (np. używa random, czas, globalne zmienne),
- Gdy nie możesz zagwarantować, że częściowe wyniki dadzą ten sam efekt po ponownym zredukowaniu.

### Używaj combinera, gdy możesz spokojnie zsumować dane lokalnie, a wynik tego sumowania można zsumować jeszcze raz — bez zmiany wyniku końcowego.
