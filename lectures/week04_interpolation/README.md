# Week 4: Data Fitting and Interpolation

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce data fitting and interpolation techniques for modeling experimental or numerical data.  
Students will learn to perform linear, polynomial, and nonlinear regression, and use interpolation for estimating unknown values.

---

## 📘 Lecture 1 – Least-Squares Regression

### Learning Outcomes
- Understand the concept of data fitting using least squares  
- Apply linear, polynomial, and multiple linear regression methods  
- Interpret regression coefficients and assess goodness of fit  
- Differentiate between linear and nonlinear regression problems  

### Lecture Flow
1. **Introduction to Data Fitting (15 min)**  
   - Motivation: experimental data, noise, and best-fit curves  
   - Difference between interpolation and regression  
   - Applications in engineering (e.g., calibration curves, trend prediction)

2. **Linear Regression (35 min)**  
   - Derivation of least-squares formulas for a straight line \( y = a_0 + a_1x \)  
   - Calculation of regression coefficients \( a_0, a_1 \)  
   - Goodness of fit: coefficient of determination \( R^2 \)  
   - *Example:* Fit a line to given data points manually or using code  

3. **Polynomial Regression (25 min)**  
   - Fitting higher-order polynomials to nonlinear data trends  
   - Overfitting and selection of polynomial order  
   - *Exercise:* Fit quadratic and cubic polynomials to a dataset  

4. **Multiple Linear Regression (25 min)**  
   - Regression with multiple independent variables  
   - Matrix form of least squares: \( \mathbf{b} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \)  
   - *Example:* Predicting performance based on two or more parameters  

5. **General Linear and Nonlinear Regression (20 min)**  
   - Transforming nonlinear relationships to linear form  
   - Iterative nonlinear regression (conceptual overview)  
   - *Example:* Exponential decay model \( y = a e^{bx} \)

6. **Summary and Discussion (10 min)**  
   - Comparison of regression types  
   - Guidelines for choosing a suitable regression model  

---

### 🎓 Assignments / Practice Ideas
- Perform linear and polynomial regression on given data (manual or Python/Excel).  
- Evaluate and compare fits using \( R^2 \) and residual plots.  
- Homework: Apply nonlinear regression to model an exponential or power-law relationship.

---

## 📘 Lecture 2 – Interpolation Techniques

### Learning Outcomes
- Understand interpolation and its difference from regression  
- Construct Newton’s and Lagrange interpolating polynomials  
- Apply spline interpolation for smooth curve fitting  
- Extend interpolation to multidimensional data  

### Lecture Flow
1. **Introduction to Interpolation (15 min)**  
   - Concept: finding intermediate values from discrete data  
   - Applications: sensor calibration, lookup tables, numerical modeling  

2. **Newton’s Divided-Difference Interpolation (35 min)**  
   - Formula and divided-difference table construction  
   - *Example:* Interpolate a missing data point using 3–4 data pairs  
   - Advantages: efficient for adding new data points  

3. **Lagrange Interpolation (25 min)**  
   - Formula derivation and implementation  
   - *Example:* Interpolate a function given 3 data points  
   - Comparison with Newton’s method  

4. **Spline Interpolation (25 min)**  
   - Concept of piecewise polynomial (cubic spline)  
   - Ensuring smoothness at data boundaries  
   - *Example:* Cubic spline fit for experimental temperature data  

5. **Additional and Inverse Interpolation (10 min)**  
   - Using interpolation for estimating x given y (inverse)  
   - Discussion of numerical stability and error  

6. **Multidimensional Interpolation (10 min)**  
   - Conceptual overview (bilinear and bicubic interpolation)  
   - Applications in surface fitting and 3D modeling  

7. **Summary & Discussion (10 min)**  
   - Comparison of interpolation methods  
   - When to use regression vs interpolation  

---

### 🎓 Suggested Homework
1. Construct a Newton divided-difference table and compute an interpolated value.  
2. Perform Lagrange interpolation for a given dataset and compare results.  
3. Use spline interpolation on data with sharp changes to observe smoothness.  
4. *(Optional)* Explore interpolation functions in software (e.g., Python `scipy.interpolate`, Excel, or MATLAB).  

---

## 🧭 Instructor Notes
- Reinforce the distinction between regression (approximation) and interpolation (exact fit).  
- Use small datasets for board work and larger ones for coding demos.  
- Show visual plots to help students interpret curve fits and interpolation behavior.  
- Encourage hands-on use of tools like Excel, MATLAB, or Python.
