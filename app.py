import asyncio

def handle_request():
    db_connection = get_db_connection()
    result = db_connection.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = result.fetchall()
    return render_template('user.html', data=user_data)