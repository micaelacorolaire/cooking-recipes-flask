CREATE TABLE public.recipe(
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    recipe_name character varying NOT NULL,
    ingredients character varying NOT NULL,
    instructions character varying NOT NULL
);

ALTER TABLE ONLY public.recipe
ADD CONSTRAINT recipe_pkey PRIMARY KEY (id_recipe) 