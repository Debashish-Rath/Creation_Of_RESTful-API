import pymysql
from app import app
from sys_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/add/category', methods=['POST'])
def add_category_details():
    try:
        json_obj = request.json
        Category_ID = json_obj['Category_ID']
        Category_Name = json_obj['Category_Name']
    
    
        if  Category_ID and Category_Name and request.method == 'POST':
            data_insertion = "INSERT INTO category(Category_ID, Category_Name) VALUES(%s, %s)"
            datas_to_be_inserted = (Category_ID, Category_Name)
            database_connection = mysql.connect()
            database_cursor = database_connection.cursor()
            database_cursor.execute(data_insertion, datas_to_be_inserted)
            print("Category Inserted")
            database_connection.commit()
            
        else:
            print("Not Inserted")
            return not_found()

    except Exception as e:
        print(str(e))
    
    
    response = jsonify('Category details added successfully !')
    response.status_code = 200
    return response
    
@app.route('/add/product', methods=['POST'])
def add_product_details():
    try:
        json_obj = request.json
        Product_ID = json_obj['Product_ID']
        Product_Name = json_obj['Product_Name']
        Product_Category_ID = json_obj['Product_Category_ID']
        Product_Category_Name = json_obj['Product_Category_Name']
        Product_Price = json_obj['Product_Price']    
    
        if  Product_ID and Product_Name and Product_Category_ID and Product_Category_Name and Product_Price and  request.method == 'POST':
            data_insertion = "INSERT INTO product(Product_ID, Product_Name, Product_Category_ID, Product_Category_Name, Product_Price) VALUES(%s, %s, %s, %s, %s)"
            datas_to_be_inserted = (Product_ID, Product_Name,Product_Category_ID, Product_Category_Name, Product_Price)
            database_connection = mysql.connect()
            database_cursor = database_connection.cursor()
            database_cursor.execute(data_insertion, datas_to_be_inserted)
            print("Product Inserted")
            database_connection.commit()
            
        else:
            return not_found()

    except Exception as e:
        print(e)
    
    
    response = jsonify('Product details added successfully !')
    response.status_code = 200
    return response


@app.route('/my_tech_store')
def store_details():
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor(pymysql.cursors.DictCursor)
        database_cursor.execute("SELECT Category_ID, Category_Name, Product_ID, Product_Name FROM category,product")
        my_store_data = database_cursor.fetchall()
        response = jsonify(my_store_data)
        response.status_code = 200
        return response
        
    
    except Exception as e:
        print(e)
    
@app.route('/my_tech_store/category')
def all_category_details():
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor(pymysql.cursors.DictCursor)
        database_cursor.execute("SELECT Category_ID, Category_Name FROM category")
        my_store_data = database_cursor.fetchall()
        response = jsonify(my_store_data)
        response.status_code = 200
        return response
        
    
    except Exception as e:
        print(e)

@app.route('/my_tech_store/product')
def all_product_details():
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor(pymysql.cursors.DictCursor)
        database_cursor.execute("SELECT Product_ID, Product_Name FROM product")
        my_store_data = database_cursor.fetchall()
        response = jsonify(my_store_data)
        response.status_code = 200
        return response
        
    
    except Exception as e:
        print(e)


@app.route('/my_tech_store/category/<int:Category_ID>', methods = ["GET"])
def get_category_details(Category_ID):
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor(pymysql.cursors.DictCursor)
        database_cursor.execute("SELECT Category_ID, Category_Name FROM category WHERE Category_ID = %s", Category_ID)
        my_store_data = database_cursor.fetchone()
        response = jsonify(my_store_data)
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)

@app.route('/my_tech_store/product/<int:Product_ID>', methods = ["GET"])
def get_product_details(Product_ID):
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor(pymysql.cursors.DictCursor)
        database_cursor.execute("SELECT Product_ID, Product_Name, Product_Category_ID, Product_Category_Name, Product_Price FROM product WHERE Product_ID =%s", Product_ID)
        my_store_data = database_cursor.fetchone()
        response = jsonify(my_store_data)
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)



@app.route('/update/category', methods=['PUT'])
def update_category():
    try:
        json_obj = request.json
        Category_ID = json_obj['Category_ID']
        Category_Name = json_obj['Category_Name']
    
    except Exception as e:
        print(e)
        
        
    # validate the received values
    if Category_Name and Category_ID and request.method == 'PUT':
        data_insertion = "UPDATE category SET Category_Name= %s WHERE Category_ID= %s"
        data_to_be_updated = (Category_Name, Category_ID,)
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor()
        database_cursor.execute(data_insertion, data_to_be_updated)
        database_connection.commit()
        
    else:
        return not_found()


    response = jsonify('Category details updated successfully !')
    response.status_code = 200
    return response


@app.route('/update/product', methods=['PUT'])
def update_product():
    try:
        json_obj = request.json
        Product_ID = json_obj['Product_ID']
        Product_Name = json_obj['Product_Name']
        Product_Category_ID = json_obj['Product_Category_ID']
        Product_Category_Name = json_obj['Product_Category_Name']
        Product_Price = json_obj['Product_Price']
    
    except Exception as e:
        print(e)
        
        
    # validate the received values
    if  Product_ID and Product_Name and Product_Category_ID and Product_Category_Name and Product_Price and request.method == 'PUT':
        data_insertion = "UPDATE product SET Product_Name = %s, Product_Category_ID = %s, Product_Category_Name = %s, Product_Price = %s WHERE Product_ID= %s"
        datas_to_be_updated = (Product_Name,Product_Category_ID, Product_Category_Name, Product_Price, Product_ID,)
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor()
        database_cursor.execute(data_insertion, datas_to_be_updated)
        database_connection.commit()
        
    else:
        return not_found()


    response = jsonify('Product details updated successfully!')
    response.status_code = 200
    return response

@app.route('/delete/category/<int:Category_ID>', methods=['DELETE'])
def delete_category(Category_ID):
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor()
        database_cursor.execute("DELETE FROM category WHERE Category_ID = %s", (Category_ID,))
        database_connection.commit()
        response = jsonify('Category details deleted successfully !')
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    
@app.route('/delete/product/<int:Product_ID>', methods=['DELETE'])
def delete_product(Product_ID):
    try:
        database_connection = mysql.connect()
        database_cursor = database_connection.cursor()
        database_cursor.execute("DELETE FROM product WHERE Product_ID = %s", (Product_ID,))
        database_connection.commit()
        response = jsonify('Product details deleted successfully !')
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    

@app.errorhandler(404)
def not_found(error=None):
    print("Inside not_found function")
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)