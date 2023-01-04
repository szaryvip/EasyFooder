-- DROP TABLE "Meals_meal_tag";
-- DROP TABLE "Users_order";
-- DROP TABLE "Meals_meal";
-- DROP TABLE "Meals_tag";

-- seedowanie posiłków
INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '1',
    'Kebab',
    15
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '2',
    'Burger',
    20
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '3',
    'Pizza',
    30
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '4',
    'Frytki',
    5
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '5',
    'Sałatka',
    20
  );

-- seedowanie tagow
INSERT INTO "Meals_tag" (tag_id, name)
VALUES (
    '1',
    'pikantne'
  );

INSERT INTO "Meals_tag" (tag_id, name)
VALUES (
    '2',
    'zdrowe'
  );

-- seedowanie powiazan tagow z posilkami
INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '1',
    '1',
    '1'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '2',
    '5',
    '2'
  );

-- seed przykladowego zamowienia
INSERT INTO "Users_order" (order_id, date, status, meal_id_id, user_id_id)
VALUES (
    '1',
    '02/01/2023',
    'Dostarczono',
    '1',
    '1'
  );
