from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import DictCursor
from .config import dsn


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/posts', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        with psycopg2.connect(**dsn) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    SELECT * FROM posts
                    """
                )
                posts = cur.fetchall()
            
        return render_template("index.html", posts=posts)

    elif request.method == 'POST':
        with psycopg2.connect(**dsn) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    INSERT INTO posts (title, content) VALUES (%s, %s)
                    
                    """, (request.form['title'], request.form['content'])
                )
        return redirect(url_for('index'))


@app.route('/<int:post_id>', methods=['POST'])
@app.route('/posts/<int:post_id>', methods=['POST'])
def delete(post_id):
    with psycopg2.connect(**dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM posts WHERE id = %s
                """, (post_id, )
            )
    return redirect(url_for('index'))


@app.before_first_request
def init_db():
    with psycopg2.connect(**dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS posts(
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )


# if __name__ == "__main__":
#     app.run(debug=True)
