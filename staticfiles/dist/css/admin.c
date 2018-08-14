@import url('https://fonts.googleapis.com/css?family=Baloo+Paaji');

body {
  margin: 0;
}

section {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Baloo Paaji', cursive;
  width: 100vw;
  height: 100vh;
  background-color: #3E3E3E;
  color: #3E3E3E;
}

.admin {
  display: flex;
  align-items: center;
  width: 350px;
  height: 250px;
  background-color: #FFFFFF;
  border-radius: 50px;
  position: relative;

  &-lock {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-color: #FFFFFF;
    border: 5px solid #FFAB00;
    right: -40px;
    top: 50%;
    margin-top: -40px;
    box-sizing: border-box;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    font-size: 50px;
    color: #3E3E3E;
    outline: none;
    cursor: pointer;
    transition: background-color 0.15s, color 0.15s;

    &:hover {
      background-color: #3E3E3E;
      color: #FFFFFF;
    }
  }

  &-content {
    border-radius: 50px;
    width: 100%;
    margin: 30px 70px 30px 30px;

    &-header {
      margin-top: 0;
    }

    .form {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      &-input {
        margin-bottom: 20px;
        outline: none;
        padding: 10px;
        border: 0;
        background-color: #E1E1E1;
        border-radius: 5px;
        font-family: 'Baloo Paaji', cursive;
        width: 100%;
        box-sizing: border-box;
        transition: box-shadow 0.15s;

        &:focus {
          box-shadow: 0 0 0 3px #FFAB00;

          &::placeholder {
            opacity: 0;
          }
        }
      }

      &-submit {
        border: 0;
        font-family: 'Baloo Paaji', cursive;
        outline: none;
        background-color: #E1E1E1;
        font-weight: bold;
        font-size: 15px;
        cursor: pointer;
        width: 120px;
        height: 50px;
        border-radius: 25px;
        transition: background-color 0.15s, color 0.15s, border 0.15s;

        &:hover {
          background-color: #3E3E3E;
          color: #FFFFFF;
          border: 3px solid #FFAB00;
        }
      }
    }
  }
}