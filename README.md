#   Profiles rest api



















1. set up a dev env
    a.vagrant - defines wat server to use - ubuntu
    b.vagrant use virtual box to create a virtual server
        i. easier to share code with users
        ii. use same versions
    c.Language - python
        i. web framework - django
        ii.  drfw - django-rest-framework
    d. Git
    e. ModHeader - modify http headers when testing api
2. set proj
3. create dev server
4. ceate django app
5. create profiles api
    a. create new profiles
        1.handle reg of new users
        2. validate profile data
    b.listing existeing profiles
        1. search for profiles by name or email
    c. view specific profiels
        1.usong prof di
    d. allow users to update name,email,password
    e. allow users to delete profiles
    f. api endpoints
        1. /api/profile/ - list all profiles on HTTP GET
        2. /api/profile/ - create new profile on HTTP POST
        3. /api/profile/{id}/ - view profile on HTTP GET
        4. /api/profile/{id}/ - update profile on HTTP PUT PATCH
        5. /api/profile/{id}/ - delete profile on HTTP DELETE
6. viewsets
    a. take care of typical logic
    b. use serializers to convert data to json
    c. perfect for dtandard db operations
    d. perform sinpmple CRUD
    e. quick and simple api
    f. working with standard db structures
7. apiviews
    a. need full control over the logic
    b. need to process files and rendder synchronous res - eg validate and return
    c. calling other apis
    d. working with local files
8. django admin
9. setup db
10. create login api
11. deploy

#VAGRANT VS DOCKER - both use virtualization technique to isolate app from the machine running on
#DOCKER - run app in light weight image - linux os,limited versions
#VAGRANT - run app in full os - ubuntu,full versions
 vagrant is more high level and uses virtualbox to create a virtual machine
 docker is more low level and uses os level virtualization to create a container
