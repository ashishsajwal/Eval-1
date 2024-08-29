{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the name:Ashish\n",
      "Enter the class:10\n",
      "Enter the height in cms:170\n",
      "Enter the weight in kgs:60\n",
      "Enter the calorie intake:2000\n",
      "Enter the sport:football\n",
      "Enter the name:Yash\n",
      "Enter the class:11\n",
      "Enter the height in cms:175\n",
      "Enter the weight in kgs:50\n",
      "Enter the calorie intake:2100\n",
      "Enter the sport:badminton\n",
      "Enter the name:Vandit\n",
      "Enter the class:12\n",
      "Enter the height in cms:170\n",
      "Enter the weight in kgs:80\n",
      "Enter the calorie intake:2000\n",
      "Enter the sport:basketball\n",
      "Ashish Green : Sufficient Intake\n",
      "Yash Green : Sufficient Ratio\n",
      "Vandit Red : Underweight\n"
     ]
    }
   ],
   "source": [
    "student = dict()\n",
    "def addStudent():\n",
    "    name=input(\"Enter the name:\")\n",
    "    Sclass=input(\"Enter the class:\")\n",
    "    height=int(input(\"Enter the height in cms:\"))\n",
    "    weight=int(input(\"Enter the weight in kgs:\"))\n",
    "    calories=int(input(\"Enter the calorie intake:\"))\n",
    "    sport=input(\"Enter the sport:\")\n",
    "    \n",
    "    student[name]={\"class\":Sclass,\"height\":height,\"weight\":weight, \"calories\":calories,\"sport\":sport}\n",
    "    \n",
    "def checkCal(name):\n",
    "    calories=student[name][\"calories\"]\n",
    "    height=student[name][\"height\"]\n",
    "    weight=student[name][\"weight\"]\n",
    "    hwratio=height/weight\n",
    "    reference=170/60\n",
    "    ans=\"Green : Sufficient Ratio\"\n",
    "    if hwratio>=reference-0.05 and hwratio<3 and calories>=2000:\n",
    "        ans=\"Green : Sufficient Intake\"\n",
    "    elif hwratio<reference-0.05 and hwratio >=reference-0.25 and calories<2200:\n",
    "        ans=\"Orange : Needs more intake\"\n",
    "    elif hwratio<reference-0.25 and calories<2400:\n",
    "        ans=\"Red : Underweight\"\n",
    "\n",
    "    return ans\n",
    "\n",
    "addStudent()\n",
    "addStudent()\n",
    "addStudent()\n",
    "\n",
    "for key,value in student.items():\n",
    "    print(key + \" \" + checkCal(key))\n",
    "    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
