# Run from root folder
docker-compose  -f docker/docker-compose-dev.yml up

# Additional docs here
`docs/index.md`

# Template.
I clone this repository `git clone https://github.com/prostomarkeloff/fastapi-tortoise`

# Plans
## Close plans
increase tests coverage

use pattern Saga for closing trouble of distrubed transaction

migrate to CBV with fastapi-utils

add scheduler for checking not runned transaction with fastapi-utils


## Future Plans
improve work with chain transaction

release work plans with refund (returning balans and trouble with negative balance after chain of transaction)

read about fraud operation 

improve logs

add pagination

add try scheduler instead fastapi work

check mongo transactions work

add https side car container

add auth(CORS, JWT токен)

add DAO and CQRS to domains

add race conditions protection 

fix TODOS

