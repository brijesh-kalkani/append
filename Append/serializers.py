from rest_framework import serializers
from .model import employeeModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeeModel
        fields = '__all__'


    def save(self):
        TradeInfo = employeeModel(empName=self.validated_data['empName'],
                mail=self.validated_data['mail'],
                salary=self.validated_data['salary'],
                )
        TradeInfo.save()
        return super().save() 