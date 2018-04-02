-- joining tables
-- join
-- find all the clients (first and last name) billing amounts and charged date
select clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
from clients
join billing on clients.id = billing.clients_id;

-- list all the domain names and leads (first and last name) for each site
select sites.domain_name, leads.first_name, leads.last_name
from sites
join leads on sites.id = leads.sites_id;

-- join on multiple tables
-- get the names of the clients, their domain name and the first names of all the leads generated from those sites
select clients.first_name as client_first, clients.last_name, sites.domain_name, leads.first_name as leads_first
from clients
join sites on clients.id = sites.clients_id
join leads on sites.id = leads.sites_id;

-- left & right join
-- list all the clients and the sites each client has, even if the client hasn't landed a site yet.
select clients.first_name, clients.last_name, sites.domain_name
from clients
left join sites on clients_id = sites.clients_id;

-- grouping rows
-- grouping by
-- sum min max avg
-- find all the clients (first and last name) and their total billing amounts
select clients.first_name, clients.last_name, sum(billing.amount)
from clients
join billing on clients.id = billing.clients_id
group by clients.id;

-- group concat
-- list all the domain names associated with each client
select group_concat(' ',sites.domain_name) as domains, clients.first_name, clients.last_name
from clients
join sites on clients.id = sites.clients_id
group by clients_id;

-- count
-- find the total number of leads for each site
select leads.id, site.domain_name
from sites
join leads on sites.id = leads.sites_id
group by sites_id;


