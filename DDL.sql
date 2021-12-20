CREATE TABLE Product_types (  
    id int PRIMARY KEY 
);  

CREATE TABLE Catalog_products (  
    id int PRIMARY KEY,  
    upc text NOT NULL, 
    description text NOT NULL, 
    brand text NOT NULL,  
    model text NOT NULL,  
    images text NOT NULL,  
    title text NOT NULL  
);  

CREATE TABLE Categories (  
    id int PRIMARY KEY NOT NULL,  
    title text NOT NULL 
);  

CREATE TABLE Sites (  
    id int PRIMARY KEY,  
    title text NOT NULL,  
    url text NOT NULL, 
    comment text NOT NULL,  
    options text NOT NULL 
);  

CREATE TABLE Supplier_categories (  
    supplier_category_id int PRIMARY KEY NOT NULL,  
    supplier_parent_category_id int,  
    app_category_id int REFERENCES Categories(Id) ON DELETE CASCADE ON UPDATE CASCADE,  
    site_id int REFERENCES Sites(Id) 
);  

CREATE TABLE Products (  
    id int PRIMARY KEY,  
    specification text NOT NULL,  
    nutrional text NOT NULL,  
    description text NOT NULL,  
    price int NOT NULL,  
    category_id int REFERENCES Categories(Id),  
    app_category_id int REFERENCES Supplier_categories(supplier_category_id),  
    catalog_product_id int REFERENCES Catalog_products(Id),  
    product_type_id int REFERENCES Product_types(Id) 
);  

CREATE TABLE Experiments_runs (  
    id int PRIMARY KEY,  
    title text NOT NULL,  
    date_start text, 
    date_stop text,  
    site_id int NOT NULL 
);  

CREATE TABLE Product_site (  
    product_id int REFERENCES Sites(Id),  
    site_id int,  
    PRIMARY KEY (product_id, site_id)  
);  

CREATE TABLE Product_category (  
    product_id int,  
    category_id int REFERENCES Categories(Id),  
    primary key (product_id, category_id)  
);    
