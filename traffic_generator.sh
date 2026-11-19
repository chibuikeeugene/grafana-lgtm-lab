for i in {1..30}; do
  curl -s -o /dev/null http://localhost:8001/orders
done

for i in {1..10}; do
  curl -s -o /dev/null http://localhost:8001/orders/error
done

for i in {1..20}; do
    curl -s -o /dev/null http://localhost:8001/orders/slow
done