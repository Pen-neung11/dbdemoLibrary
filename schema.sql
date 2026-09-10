-- เฉลย schema ระบบห้องสมุด (ห้ามแจกนิสิต)

DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS loan;
DROP TABLE IF EXISTS book_copy;
DROP TABLE IF EXISTS book_title;
DROP TABLE IF EXISTS member;


-- =========================================
-- Table: member
-- =========================================

CREATE TABLE member (
    member_id   INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    gender      CHAR(1),
    email       VARCHAR(120) UNIQUE,
    phone       VARCHAR(20),
    member_type VARCHAR(10) DEFAULT 'regular'
);


-- =========================================
-- Table: book_title
-- =========================================

CREATE TABLE book_title (
    title_id     INT AUTO_INCREMENT PRIMARY KEY,
    title        VARCHAR(200) NOT NULL,
    author       VARCHAR(120),
    category     VARCHAR(60),
    publish_year INT
);


-- =========================================
-- Table: book_copy
-- =========================================

CREATE TABLE book_copy (
    copy_id       INT AUTO_INCREMENT PRIMARY KEY,
    title_id      INT NOT NULL,
    status        VARCHAR(12) DEFAULT 'available',
    shelf_location VARCHAR(30),

    FOREIGN KEY (title_id)
        REFERENCES book_title(title_id)
);


-- =========================================
-- Table: loan
-- =========================================

CREATE TABLE loan (
    loan_id    INT AUTO_INCREMENT PRIMARY KEY,
    member_id  INT NOT NULL,
    copy_id    INT NOT NULL,
    loan_date  DATE NOT NULL,
    due_date   DATE NOT NULL,
    return_date DATE,

    FOREIGN KEY (member_id)
        REFERENCES member(member_id),

    FOREIGN KEY (copy_id)
        REFERENCES book_copy(copy_id)
);


-- =========================================
-- Table: reservation
-- =========================================

CREATE TABLE reservation (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id      INT NOT NULL,
    title_id       INT NOT NULL,
    reserve_date   DATE,
    status         VARCHAR(12) DEFAULT 'waiting',

    FOREIGN KEY (member_id)
        REFERENCES member(member_id),

    FOREIGN KEY (title_id)
        REFERENCES book_title(title_id)
);


-- =========================================
-- Insert: member
-- =========================================

INSERT INTO member (
    name,
    gender,
    email,
    phone,
    member_type
)
VALUES
    ('Somchai', 'M', 'somchai@mail.com', '0810000001', 'VIP'),
    ('Suda',    'F', 'suda@mail.com',    '0810000002', 'regular'),
    ('Anan',    'M', 'anan@mail.com',    '0810000003', 'regular'),
    ('Ploy',    'F', 'ploy@mail.com',    '0810000004', 'VIP'),
    ('Kan',     'M', 'kan@mail.com',     '0810000005', 'regular');


-- =========================================
-- Insert: book_title
-- =========================================

INSERT INTO book_title (
    title,
    author,
    category,
    publish_year
)
VALUES
    ('Database System Concepts', 'Silberschatz',       'Database',    2020),
    ('Clean Code',               'Robert Martin',      'Programming', 2008),
    ('SQL Cookbook',             'Anthony Molinaro',   'Database',    2005),
    ('Sapiens',                  'Yuval Harari',       'History',     2011),
    ('The Pragmatic Programmer',  'Hunt & Thomas',      'Programming', 1999);


-- =========================================
-- Insert: book_copy
-- =========================================

INSERT INTO book_copy (
    title_id,
    status,
    shelf_location
)
VALUES
    (1, 'borrowed',  'A1'),
    (1, 'borrowed',  'A1'),
    (2, 'available', 'A2'),
    (3, 'borrowed',  'B1'),
    (4, 'available', 'C1'),
    (5, 'borrowed',  'B2');


-- =========================================
-- Insert: loan
-- =========================================

INSERT INTO loan (
    member_id,
    copy_id,
    loan_date,
    due_date,
    return_date
)
VALUES
    (1, 1, '2026-05-01', '2026-05-15', NULL),
    (2, 4, '2026-06-01', '2026-06-15', NULL),
    (1, 2, '2026-06-10', '2026-06-24', NULL),
    (1, 6, '2026-04-10', '2026-04-24', '2026-04-20'),
    (3, 4, '2026-03-01', '2026-03-15', '2026-03-14'),
    (2, 1, '2026-02-01', '2026-02-15', '2026-02-10');


-- =========================================
-- Insert: reservation
-- =========================================

INSERT INTO reservation (
    member_id,
    title_id,
    reserve_date,
    status
)
VALUES
    (2, 1, '2026-06-20', 'waiting'),
    (3, 1, '2026-06-21', 'waiting');
    
    