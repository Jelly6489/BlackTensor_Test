import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
# from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
import datetime

class ExchangeAi(object):

    def create(self):
        print('============ Test AI1 ============')
        st_data = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0])
        st_data.drop(['keyword'], axis='columns', inplace=True)
        # st_data.head()

        ex_data = pd.read_csv('./csv/exchange_index.csv', index_col=[0])
        ex_data.drop(['date', 'jpy', 'eur', 'cny'], axis='columns', inplace=True)
        df = pd.concat([st_data, ex_data], axis=1)
        
        high_price = df['high'].values
        low_price = df['low'].values
        mid_price = (high_price + low_price) /2

        # 최근 50일 데이터를 다음을 예측
        # 50개를 보고 예측하기 때문에 51개씩 저장
        seq_len = 50
        sequence_length = seq_len + 1
        print('============ Test AI2 ============')
        result = []
        for index in range(len(mid_price) - sequence_length):
            result.append(mid_price[index: index + sequence_length])
            
        try:
            normalized_data = []
            for window in result:
                normalized_window = [((float(p) / float(window[1])) - 1) for p in window]
                normalized_data.append(normalized_window)
        except:
            print('예외 발생!')

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]

        x_train.shape, x_test.shape
        print('============ Test AI3 ============')
        model = Sequential()

        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))

        model.add(LSTM(64, return_sequences=False))

        model.add(Dense(1, activation='linear'))

        model.compile(loss='mse', optimizer='rmsprop')
        # model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])

        model.summary()

        model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=20)
        # print('정확도 : %.4f' % (model.evaluate(x_train, y_train)[1]))

        pred = model.predict(x_test)
        print('============ Test AI4 ============')
        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(y_test, label='True')
        ax.plot(pred, label='Prediction')
        plt.title('Stock & USD LSTM')
        ax.legend()
        plt.show()
        print('============ Test AI5 ============')
    create(0)