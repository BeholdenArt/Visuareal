from math import floor
from Company.models import OrderQueue
from Users.models import User
from Company.models import CompanyInventory, AddCustomer
from Points.models import ExtraPoints

def Points(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        if user is not None:
            pdts = OrderQueue.objects.all()
            usr = pdts.last().user
            points = int(usr.totalPoints)

            pdt_quantity = pdts.last().orderedQuantity
            # pdt_quantity = OrderQueue.objects.filter(user= user).values('orderedQuantity')
            pdts = pdts.last().orderedProducts
            # print(pdts)
            # print('--'*10,pdts)
            # print(OrderQueue.objects.filter(user= user))
            pdt_points = list(CompanyInventory.objects.filter(productName = pdts).values_list('point', flat=True))
            print(pdt_points)
            ext_points = list(ExtraPoints.objects.filter(product = pdts).values_list('festival', 'occasion', 'misc', 'geography'))
            print(ext_points)
            print(sum(ext_points[0]) + sum(pdt_points))
            
            print(pdt_quantity)
            points += (sum(ext_points[0]) + sum(pdt_points))*pdt_quantity

            usr.totalPoints = points
            usr.save()

            # print(temp_sum)

def influencer_points(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        if user is not None:
            cust = AddCustomer.objects.all()
            usr = cust.last().user
            points = int(usr.totalPoints)
            print(cust.last().interestedProduct)
            intrested_pdt = cust.last().interestedProduct
            pdt_points = list(CompanyInventory.objects.filter(productName = intrested_pdt).values_list('point', flat=True))
            print(pdt_points)
            points += sum(pdt_points) + floor(0.30*sum(pdt_points))

            usr.totalPoints = points
            usr.save()
            
def tier(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        if user is not None:
            if user.totalPoints >= 30000:
                return "elite"
            elif user.totalPoints >= 15000:
                return "platinum"
            elif user.totalPoints >= 5000:
                return "gold"
            elif user.totalPoints >= 1000:
                return "silver"
            else:
                return "bronze"