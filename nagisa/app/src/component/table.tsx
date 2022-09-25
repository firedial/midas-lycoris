import React from 'react';
import styles from './table.module.css';

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
      <tr>
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
              <td>{balance.id}</td>
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
    </table >
  )
}

export { BalanceTable };
