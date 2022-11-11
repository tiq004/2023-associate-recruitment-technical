select owner.owner_id, owner.owner_name, COUNT(DISTINCT category_article_mapping.category_id) AS different_category_count
FROM article
Left Join owner on owner.owner_id = article.owner_id
LEFT JOIN category_article_mapping ON category_article_mapping.article_id = article.article_id
ORDER BY COUNT(DISTINCT category_article_mapping.category_id) DESC