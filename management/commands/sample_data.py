from django.core.management.base import BaseCommand,CommandError
from users.models import CustomUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        return super().handle(*args, **options)    
    
    def add_arguments(self, parser):
        return super().add_arguments(parser)
    

    def create_users(self,args,options):
        list_users = [
           # security_lic, Firstname,Lastname,email,role,department,status,password
            '23456789,Olivia,Chen,olivia.chen@example.com,AD,CN,active,Secure@1234',
            '34567890,Liam,Patel,liam.patel@example.com,MR,EN,active,Secure@1234',
            '45678901,Emma,Garcia,emma.garcia@example.com,SR,EN,active,Secure@1234',
            '56789012,Noah,Singh,noah.singh@example.com,NR,CN,inactive,Secure@1234',
            '67890123,Ava,Kim,ava.kim@example.com,NR,EN,active,Secure@1234',
            '78901234,William,Rodriguez,william.r@example.com,MR,CN,active,Secure@1234',
            '89012345,Sophia,Martinez,sophia.martinez@example.com,NR,EN,active,Secure@1234',
            '90123456,James,Lee,james.lee@example.com,SR,CN,inactive,Secure@1234',
            '11223344,Isabella,Brown,isabella.b@example.com,NR,CN,active,Secure@1234',
            '22334455,Benjamin,Wilson,ben.wilson@example.com,NR,EN,active,Secure@1234',
            '33445566,Mia,Tremblay,mia.tremblay@example.com,AD,EN,active,Secure@1234',
            '44556677,Lucas,Gagnon,lucas.gagnon@example.com,MR,EN,inactive,Secure@1234',
            '55667788,Charlotte,Roy,charlotte.roy@example.com,NR,CN,active,Secure@1234',
            '66778899,Henry,Lefebvre,henry.l@example.com,SR,EN,active,Secure@1234',
            '77889900,Amelia,Cote,amelia.cote@example.com,NR,CN,inactive,Secure@1234'
        ]


        self.style.NOTICE("Creating sample employes with following security_lic, Firstname,Lastname,email,role,department,status..........")

        for user in list_users:
            user  = user.split(',')
            try:
                CustomUser.objects.create(
                    sec_id=user[0],
                    firstname=user[1],
                    lastname=user[2],
                    email=user[3],
                    password=user[7]

                )
            except :
                self.style.ERROR("User Not Create -",user[1]+user[2])
        