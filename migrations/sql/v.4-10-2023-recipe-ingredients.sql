CREATE TABLE public.recipe_ingredients(
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    ingredient character varying NOT NULL,
    quantity integer NOT NULL
);

ALTER TABLE ONLY public.recipe_ingredients
ADD CONSTRAINT recipe_ingredients_pkey PRIMARY KEY (id_recipe_ingredients) 