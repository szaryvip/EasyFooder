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
    'Sałatka grecka',
    20
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '6',
    'GigaKanapka',
    22
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '7',
    'Tosty',
    24
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '8',
    'Sushi',
    56
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '9',
    'Stek',
    70
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '10',
    'Krewetki grilowane',
    40
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '11',
    'Krewetki na ostro',
    42
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '12',
    'Tosty ala Diablo',
    29
  );

INSERT INTO "Meals_meal" (meal_id, name, price)
VALUES (
    '13',
    'Sałatka paryska',
    26
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

INSERT INTO "Meals_tag" (tag_id, name)
VALUES (
    '3',
    'fast food'
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

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '3',
    '11',
    '1'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '4',
    '12',
    '1'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '5',
    '13',
    '2'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '6',
    '1',
    '3'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '7',
    '2',
    '3'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '8',
    '3',
    '3'
  );

INSERT INTO "Meals_meal_tag" (id, meal_id_id, tag_id_id)
VALUES (
    '9',
    '4',
    '3'
  );

-- seed przykladowego zamowienia
INSERT INTO "Meals_order" (order_id, date, status, meal_id_id, user_id_id)
VALUES (
    '1',
    '02/01/2023',
    'Dostarczono',
    '1',
    '1'
  );
