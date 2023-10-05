CREATE TABLE public.ingredients(
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    ingredients_name character varying NOT NULL
);

ALTER TABLE ONLY public.ingredients
ADD CONSTRAINT ingredients_pkey PRIMARY KEY (id) 