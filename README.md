<h1 align="center"> Django Framework - Fresher Training - IIR Lab</h1>

<!DOCTYPE html>
<html>
<head>
</head>
<body>

<h2> Project Title: Movie Rating Database .</h2>

</body>
</html>


![](https://raw.githubusercontent.com/phanben110/IIR_Django_Movie_Rating/master/images/demo.gif)

## 1. How to deploy project
### Step 1: Clone repository and checkout master branch
```bash
git clone https://github.com/phanben110/IIR_Django_Movie_Rating
cd IIR_Django_Movie_Rating
git branch
```
### Step 2: Build docker images
```bash
bash setup.sh
```
### Step 3: Run docker images
```bash
bash docker_run.sh demo-django
```
### Step 4: Check logs from docker 
```bash
docker logs -f demo-django
```
### Step 5: Open website in browser with link http http://localhost:8000/ratings/

## 2. Video demo
[Video Demo](https://youtu.be/14m8RKSdxQY) 


## 3. Authors
Contributors names and contact info

* [Phan Ben](https://www.facebook.com/benphan110) - Master's degree in Computer Science at National Cheng Kung University - Email: phanben110@gmail.com

## 5. Acknowledgments

* [Django Framework ](https://www.djangoproject.com/)
