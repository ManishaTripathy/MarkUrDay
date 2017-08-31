drop table if exists users;
create table users (
  uid integer primary key autoincrement,
  name text not null,
  email text unique not null,
  password text not null
);

drop table if exists calendars;
create table calendar(
  cid integer primary key autoincrement,
  c_date date not null,
  flag boolean,
  ref_id integer not null,
  foreign key(ref_id) references users(uid)
);
