SELECT 
    COUNT(*) AS total_tabelas
FROM information_schema.tables
WHERE table_schema = 'analytics';


SELECT 
    table_name
FROM information_schema.tables
WHERE table_schema = 'analytics'
ORDER BY table_name;


SELECT 'customers' AS tabela, COUNT(*) AS registros FROM analytics.customers
UNION ALL
SELECT 'restaurants', COUNT(*) FROM analytics.restaurants
UNION ALL
SELECT 'cities', COUNT(*) FROM analytics.cities
UNION ALL
SELECT 'fixed_costs', COUNT(*) FROM analytics.fixed_costs
UNION ALL
SELECT 'orders', COUNT(*) FROM analytics.orders;
