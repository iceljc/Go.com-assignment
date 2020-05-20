import pandas as pd
import xlrd

def read_data(file):
	data = pd.read_excel(file)
	df = pd.DataFrame(data)

	cars_rev, boats_rev, planes_rev = [], [], []
	data_len = df.shape[0]

	for i in range(data_len):
		if df['Product Line'][i] == 'Cars.go.com':
			cars_rev.append(round(df['Revenue'][i],2))
			# print(df['Revenue'][i])
		elif df['Product Line'][i] == 'Boats.go.com':
			boats_rev.append(round(df['Revenue'][i],2))
		elif df['Product Line'][i] == 'Planes.go.com':
			planes_rev.append(round(df['Revenue'][i],2))

	print(len(cars_rev), len(boats_rev), len(planes_rev))
	return cars_rev, boats_rev, planes_rev


def read_histroy():
	history_rev, history_profit = {}, {}
	history_rev['cars'] = [6085063, 5663582, 5701994, 5691910, 5906352]
	history_rev['boats'] = [4329578, 4418088, 4657184, 4597765, 5437214]
	history_rev['planes'] = [32339403, 34861524, 36039564, 34422242, 45337642]

	history_profit['cars'] = [608506.3, 566358.2, 570199.4, 569191, 590635.2]
	history_profit['boats'] = [86591.56, 88361.76, 93143.68, 91955.3, 108744.28]
	history_profit['planes'] = [161697.015, 174307.62, 180197.82, 172111.21, 226688.21]


	return history_rev, history_profit



if __name__ == '__main__':
	
	cars_rev, boats_rev, planes_rev = read_data('data.xlsx')
	cars_rev_sum = sum(cars_rev)
	boats_rev_sum = sum(boats_rev)
	planes_rev_sum = sum(planes_rev)

	history_rev, history_profit = read_histroy()

	# idx = 4
	# print(history_rev['cars'][idx] + history_rev['boats'][idx] + history_rev['planes'][idx])
	# print(history_profit['cars'][idx] + history_profit['boats'][idx] + history_profit['planes'][idx])	

	# for item in history_rev:
	# 	for i in range(len(history_rev[item])):
	# 		print(item, history_profit[item][i] / history_rev[item][i])


	cars_ratio = history_profit['cars'][0] / history_rev['cars'][0]
	boats_ratio = history_profit['boats'][0] / history_rev['boats'][0]
	planes_ratio = history_profit['planes'][0] / history_rev['planes'][0]
	print(cars_ratio, boats_ratio, planes_ratio)

	cars_profit = cars_ratio * cars_rev_sum
	boats_profit = boats_ratio * boats_rev_sum
	planes_profit = planes_ratio * planes_rev_sum

	print('Cars - Revenue: {:.2f}, Profit: {:.2f}'.format(cars_rev_sum, cars_profit))
	print('Boats - Revenue: {:.2f}, Profit: {:.2f}'.format(boats_rev_sum, boats_profit))
	print('Planes - Revenue: {:.2f}, Profit: {:.2f}'.format(planes_rev_sum, planes_profit))

	print('Total profit: {:.2f}'.format(sum([cars_profit, boats_profit, planes_profit])))


