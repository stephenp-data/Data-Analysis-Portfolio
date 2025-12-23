SELECT
    c.customer_unique_id,
    SUM(p.payment_value) AS lifetime_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY lifetime_value DESC;
