from django.db import models

# Create your models here.
class Endpoint(models.Model):

    name = models.CharField(max_length = 128)
    owner = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add = True, blank= True)


class MLAlgorithm(models.Model):

     name = models.CharField(max_length = 128)
     description = models.CharField(max_length = 1000)
     code = models.CharField(max_length = 50000)
     version = models.CharField(max_length = 128)
     owner = models.CharField(max_length = 128)
     created_at = models.DateTimeField(auto_now_add = True, blank = True)
     parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):

    status= models.CharField(max_length = 128)
    active = models.BooleanField()
    created_by = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete = models.CASCADE)

class MLRequest(models.Model):

    input_data = models.CharField(max_length = 10000)
    full_response = models.CharField(max_length = 10000)
    response = models.CharField(max_length = 10000)
    feedback = models.CharField(max_length = 10000, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    parent_mlagorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)



