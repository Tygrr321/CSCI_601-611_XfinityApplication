# Import necessary libraries

from flask import Flask, render_template

import psycopg2

import pytest


app = Flask(__name__)


    # Successfully establish connection to PostgreSQL database with valid credentials
def jls_extract_def(mocker, mock_psycopg2, mock_conn, connect_db, dbname, user, password, host, port, result):
    def test_successful_db_connection(self, mocker):
            # Arrange
            mock_psycopg2 = mocker.patch('psycopg2.connect')
            mock_conn = mocker.Mock()
            mock_psycopg2.return_value = mock_conn
    
            # Act
            result = connect_db()
    
            # Assert
            mock_psycopg2.assert_called_once_with(
                dbname="XfinityApp",
                user="postgres", 
                password="Postgrer00t",
                host="localhost",
                port="5432"
            )
            assert result == mock_conn
    return result


result = jls_extract_def(mocker, mock_psycopg2, mock_conn, connect_db, dbname, user, password, host, port, result)
@app.route('/')

    # Handle invalid database credentials
def test_invalid_credentials_raises_error(self, mocker):
        # Arrange
        mock_psycopg2 = mocker.patch('psycopg2.connect')
        mock_psycopg2.side_effect = psycopg2.OperationalError("Invalid credentials")

        # Act & Assert
        with pytest.raises(psycopg2.OperationalError) as exc_info:
            connect_db()
        assert "Invalid credentials" in str(exc_info.value)

def index():
    # Route for the home page that fetches data from the database
    # and renders the 'index.html' template with the fetched data.

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Appointments")

    appointments = cursor.fetchall()

    cursor.close()

    conn.close()

    return render_template('index.html', appointments=appointments)


if __name__ == '__main__':

    # Run the Flask application in debug mode

    app.run(debug=True)

