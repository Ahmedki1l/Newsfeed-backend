from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

# Add a new post
@app.route('/posts', methods=['POST'])
def add_post():
    content = request.json['content']
    user_id = request.json['user_id']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Posts (user_id, content) VALUES (%s, %s)', (user_id, content))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post added successfully'}), 201

# Update a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    content = request.json['content']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Posts SET content = %s WHERE id = %s', (content, post_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post updated successfully'})

# Delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Posts WHERE id = %s', (post_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post deleted successfully'})

# Get a post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Posts WHERE id = %s', (post_id,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()

    if post:
        return jsonify({'post': post})
    else:
        return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
