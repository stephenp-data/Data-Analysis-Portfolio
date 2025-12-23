-- Purpose:
-- Calculate monthly revenue trends to evaluate business growth over time.

SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    SUM(payment_value) AS revenue
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;
