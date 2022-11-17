#!/bin/bash

echo '_____НАЧИНАЕМ______'
echo "1. Общее количество запросов"
cat access.log | wc -l | awk '{print $1}'
echo '___________________'

echo "2. Общее количество запросов по типу"
cat access.log | awk '{print$6}' | sed 's,",запросов ,' | sort | uniq -c | sort -rnk1 | sed '$d'
echo '___________________'

echo "3. Топ 10 самых частых запросов"
cat access.log | awk '{print$7}' | sort | uniq -c | sort -rnk1 | head -n 10
echo '___________________'

echo "4. Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой"
cat access.log | awk '{if ($9 ~ /4../) {print $7, $9, $10, $1}}' | sort -rnk3 | head -n 5
echo '___________________'

echo "5. Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой"
cat access.log | awk '{if ($9 ~ /5../) {print $1}}' | sort | uniq -c | sort -rnk1 | head -n 5
echo '______THE END______'
