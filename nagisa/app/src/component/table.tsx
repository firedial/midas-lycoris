import React from 'react';
import styles from './table.module.scss';

type BalanceData = {
  id: number
  amount: number
  item: string
  kind_element_id: number
  purpose_element_id: number
  place_element_id: number
  date: string
}

const BalanceTable = (props: { balances: BalanceData[] }) => {
  return (
    <table className={styles.tableStyle}>
      <tbody>
        <tr className={styles.trThStyle}>
          <th>Id</th>
          <th>Amount</th>
          <th>Item</th>
          <th>KindElementId</th>
          <th>PurposeElementId</th>
          <th>PlaceElementId</th>
          <th>Date</th>
        </tr>
        {
          props.balances.map((balance) => {
            return (
              <tr key={balance.id}>
                <td><a href={'/balances/' + balance.id}>{balance.id}</a></td>
                <td>{balance.amount}</td>
                <td>{balance.item}</td>
                <td>{balance.kind_element_id}</td>
                <td>{balance.purpose_element_id}</td>
                <td>{balance.place_element_id}</td>
                <td>{balance.date}</td>
              </tr>
            )
          })
        }
        <tr className={styles.lastTrStyle} key='new'>
          <td><a href='/balances/create'>+</a></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table >
  )
}

export { BalanceTable };
