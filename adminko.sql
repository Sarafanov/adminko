--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: category; Type: TABLE; Schema: public; Owner: ivan; Tablespace: 
--

CREATE TABLE category (
    id integer NOT NULL,
    name character varying(80)
);


ALTER TABLE public.category OWNER TO ivan;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: ivan
--

CREATE SEQUENCE category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO ivan;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ivan
--

ALTER SEQUENCE category_id_seq OWNED BY category.id;


--
-- Name: managers; Type: TABLE; Schema: public; Owner: ivan; Tablespace: 
--

CREATE TABLE managers (
    user_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.managers OWNER TO ivan;

--
-- Name: product; Type: TABLE; Schema: public; Owner: ivan; Tablespace: 
--

CREATE TABLE product (
    id integer NOT NULL,
    name character varying(50),
    articul character varying(50),
    price integer,
    description character varying(500),
    category_id integer
);


ALTER TABLE public.product OWNER TO ivan;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: ivan
--

CREATE SEQUENCE product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO ivan;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ivan
--

ALTER SEQUENCE product_id_seq OWNED BY product.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: ivan; Tablespace: 
--

CREATE TABLE "user" (
    id integer NOT NULL,
    name character varying(80),
    "isAdmin" boolean
);


ALTER TABLE public."user" OWNER TO ivan;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: ivan
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO ivan;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ivan
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY category ALTER COLUMN id SET DEFAULT nextval('category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY product ALTER COLUMN id SET DEFAULT nextval('product_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: ivan
--

COPY category (id, name) FROM stdin;
1	Стиральные машины
2	Телевизоры
3	Ноутбуки
4	Смартфоны
5	Велосипеды
6	Мягкие игрушки
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ivan
--

SELECT pg_catalog.setval('category_id_seq', 10, true);


--
-- Data for Name: managers; Type: TABLE DATA; Schema: public; Owner: ivan
--

COPY managers (user_id, category_id) FROM stdin;
4	1
4	2
4	5
8	6
3	3
3	5
3	6
2	1
2	4
2	5
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: ivan
--

COPY product (id, name, articul, price, description, category_id) FROM stdin;
1	Bosch WLG 20060	AL-238690	17000		1
2	Indesit IWUB 4085	AL-235617	11155		1
3	LG F-1096ND3	AL-231037	21670		1
4	Indesit IWUC 4170	AL-251605	11290		1
5	Hotpoint-Ariston VMSL 501	AL-247727	12999		1
6	Siemens WS 10G160	AL-252645	20447		1
7	Bosch WLG 20160	AL-239574	19300		1
8	Bosch WLG 20061	AL-234780	17770		1
9	LG F-10B8MD	AL-271422	19892		1
10	Candy GC4 1051 D	AL-271521	12764		1
11	Indesit IWUC 4005	AL-234512	98570		1
12	LG F-1296ND4	AL-231699	23085		1
13	LG F-12B8QD5	AL-242642	22197		1
14	Indesit IWUC 4125	AL-253085	15741		1
15	Samsung UE32J4000AU	AE-560971	13999		2
16	LG 43UH619V	AE-168471	29592		2
17	49UH610V	AE-128001	35590		2
37	Meizu MX6	SM-448312	20694	смартфон, Android 6.0\r\nподдержка двух SIM-карт\r\nэкран 5.5", разрешение 1920x1080\r\nкамера 12 МП, автофокус\r\nпамять 32 Гб, без слота для карт памяти	4
21	STELS Energy II 26 (2016)	AA-123450	34067	городской велосипед\r\nразмер рамы: 16.0 дюйм\r\nрама: алюминиевый сплав\r\nколеса 26 дюймов 	5
22	LG 32LH530V	TV-451300	16100	ЖК-телевизор, 1080p Full HD\r\nдиагональ 32" (81 см)\r\nHDMI x2, USB, DVB-T2\r\nтип подсветки: Direct LED\r\n2 TV-тюнера	2
23	Samsung UE22H5600	TV-984311	13550	ЖК-телевизор, 1080p Full HD\r\nдиагональ 22" (56 см)\r\nSmart TV, Wi-Fi\r\nHDMI x3, USB x2, DVB-T2\r\nкартинка в картинке	2
24	Samsung UE40K6500AU	TV-345007	34000	ЖК-телевизор, 1080p Full HD\r\nдиагональ 40" (102 см)\r\nSmart TV, Wi-Fi\r\nHDMI x3, USB x2, DVB-T2\r\nизогнутый экран\r\nкартинка в картинке	2
25	Samsung UE49K5510AW	TV-495510	41941	ЖК-телевизор, 1080p Full HD\r\nдиагональ 49" (124 см)\r\nSmart TV, Wi-Fi\r\nHDMI x3, USB x2, DVB-T2\r\nкартинка в картинке	2
26	Samsung UE19H4000	TV-136702	11139	ЖК-телевизор, 720p HD\r\nдиагональ 19" (48 см)\r\nHDMI x2, USB x2, DVB-T2\r\nкартинка в картинке	2
27	ASUS K501UX	NT-345109	52779	Процессор: Core i5 / Core i7\r\nЧастота процессора: 2300...2500 МГц\r\nОбъем оперативной памяти: 4...16 Гб\r\nОбъем жесткого диска: 256...1256 Гб\r\nРазмер экрана: 15.6 "	3
28	DELL INSPIRON 3558	NT-347800	23645	Процессор: Celeron / Core i3 / Core i5\r\nЧастота процессора: 1600...2200 МГц\r\nОбъем оперативной памяти: 4 Гб\r\nОбъем жесткого диска: 500...1000 Гб\r\nРазмер экрана: 15.6 "	3
29	Apple MacBook Air 13	NT-120067	85900	Процессор: Core i5\r\nЧастота процессора: 1600...2200 МГц\r\nОбъем оперативной памяти: 8 Гб\r\nОбъем жесткого диска: 128...512 Гб\r\nРазмер экрана: 13.3 "	3
30	Apple MacBook Early 2016	NT-905612	128990	Процессор: Core M3 / Core M5\r\nЧастота процессора: 1100...1200 МГц\r\nОбъем оперативной памяти: 8 Гб\r\nОбъем жесткого диска: 256...512 Гб\r\nРазмер экрана: 12 "	3
31	ASUS VivoBook Max X541SA	NT-461056	24038	Процессор: Celeron / Pentium\r\nЧастота процессора: 1600 МГц\r\nОбъем оперативной памяти: 2...4 Гб\r\nОбъем жесткого диска: 500 Гб\r\nРазмер экрана: 15.6 "	3
32	Apple iPhone 7 128Gb	SM-341077	62732	смартфон, iOS 10\r\nэкран 4.7", разрешение 1334x750\r\nкамера 12 МП, автофокус\r\nпамять 128 Гб, без слота для карт памяти\r\n3G, 4G LTE, LTE-A, Wi-Fi, Bluetooth, NFC, GPS, ГЛОНАСС\r\nобъем оперативной памяти 2 Гб	4
33	Xiaomi Redmi 4 Pro	SM-834412	12490	смартфон, Android 6.0\r\nподдержка двух SIM-карт\r\nэкран 5", разрешение 1920x1080\r\nкамера 13 МП, автофокус\r\nпамять 32 Гб, слот для карты памяти	4
34	Samsung Galaxy S7 32Gb	SM-605180	40020	смартфон, Android 6.0\r\nподдержка двух SIM-карт\r\nэкран 5.1", разрешение 2560x1440\r\nкамера 12 МП, автофокус\r\nпамять 32 Гб, слот для карты памяти	4
35	НОВИНКАSamsung Galaxy A5	SM-120076	25509	смартфон на платформе Android\r\nподдержка двух SIM-карт\r\nэкран 5.2", разрешение 1920x1080\r\nкамера 16 МП, автофокус\r\nпамять 32 Гб, слот для карты памяти	4
36	Xiaomi Mi5 32GB	SM-109367	21671	смартфон, Android 6.0\r\nподдержка двух SIM-карт\r\nэкран 5.15", разрешение 1920x1080\r\nкамера 16 МП, автофокус\r\nпамять 32 Гб, без слота для карт памяти	4
38	ASUS Zenfone 3 ZE552KL	SM-542853	27990		4
39	CHALLENGER Genesis	BC-450924	9690	велосипед для кросс-кантри\r\nразмер рамы: 16, 18, 20 дюйм\r\nрама: сталь\r\nколеса 26 дюймов\r\nдвухподвесный\r\n18 скоростей	5
40	STELS Navigator 530	BC-392340	15253	велосипед для кросс-кантри\r\nразмер рамы: 16.0, 18.0, 20.0 дюйм\r\nрама: алюминиевый сплав\r\nколеса 26 дюймов	5
41	Scott Plasma Premium (2016)	BC-901788	734948	шоссейный велосипед\r\nразмер рамы: 20.47, 21.25, 22.04, 22.83 дюйм\r\nрама: карбон (углепластик)\r\nколеса 28 дюймов\r\nRigid (жесткий)\r\n22 скорости	5
42	STELS Navigator 500	BC-401099	12120	велосипед для кросс-кантри\r\nразмер рамы: 16.0, 18.0, 20.0 дюйм\r\nрама: сталь\r\nколеса 26 дюймов\r\nHard tail	5
44	Мягкая игрушка Gulliver	TO-482533	2409	Производитель: Gulliver\r\nТип: дикие животные	6
45	Мягкая игрушка Orange Toys	TO-520677	830	Производитель: Orange Toys\r\nВысота: 40 см	6
47	Мягкая игрушка Guliver	TO-205480	1370	Производитель: Gulliver\r\nТип: домашние животные\r\nПол: для девочки, для мальчика	6
48	Мягкая игрушка Мульти-Пульти	TO-401193	709	Производитель: Мульти-Пульти\r\nТип: герои мультфильмов\r\nПерсонаж: Чебурашка	6
50	Мягкая игрушка Orange Toy	TO-294419	1290	Производитель: Orange Toys\r\nТип: домашние животные, кошки\r\nПол: для девочки, для мальчика	6
43	Merida Matts 6. 40-D (2015)	BC-429107	26500	 велосипед для кросс-кантри\r\nразмер рамы: 14.5, 16.0, 18.0, 20.0, 22.0, 24.0 дюйм\r\nрама: алюминиевый сплав\r\nколеса 26 дюймов 	5
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ivan
--

SELECT pg_catalog.setval('product_id_seq', 55, true);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: ivan
--

COPY "user" (id, name, "isAdmin") FROM stdin;
1	admin	t
2	manager1	f
3	manager2	f
4	manager3	f
5	manager4	f
6	manager5	f
7	manager6	f
8	Jon Snow	f
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ivan
--

SELECT pg_catalog.setval('user_id_seq', 8, true);


--
-- Name: category_name_key; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_name_key UNIQUE (name);


--
-- Name: category_pkey; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: managers_pkey; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY managers
    ADD CONSTRAINT managers_pkey PRIMARY KEY (user_id, category_id);


--
-- Name: product_articul_key; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_articul_key UNIQUE (articul);


--
-- Name: product_pkey; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: user_name_key; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_name_key UNIQUE (name);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: public; Owner: ivan; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: managers_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY managers
    ADD CONSTRAINT managers_category_id_fkey FOREIGN KEY (category_id) REFERENCES category(id);


--
-- Name: managers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY managers
    ADD CONSTRAINT managers_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id);


--
-- Name: product_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ivan
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_category_id_fkey FOREIGN KEY (category_id) REFERENCES category(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

