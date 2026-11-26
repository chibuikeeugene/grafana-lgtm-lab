for i in {1..30}; do
  curl -s -o /dev/null http://localhost:8022/orders
done

for i in {1..10}; do
  curl -s -o /dev/null http://localhost:8022/orders/error
done

for i in {1..20}; do
    curl -s -o /dev/null http://localhost:8022/orders/slow
done