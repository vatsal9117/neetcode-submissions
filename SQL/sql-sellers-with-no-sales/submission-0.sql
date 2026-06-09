SELECT s.seller_name
FROM seller s
where s.seller_id NOT IN (
    select seller_id
    FROM orders
    where sale_date >= '2020-01-01' and sale_date <= '2020-12-31')
ORDER BY s.seller_name ASC;