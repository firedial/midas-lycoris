import React from 'react';
import styles from './table.module.scss';

type BalanceData = {
  id?: number
  amount?: number
  item?: string
  kind_element_id?: number
  purpose_element_id?: number
  place_element_id?: number
  date?: string
}

const BalanceDetail = (props: { balance?: BalanceData }) => {
  return (
    <table>
      <tbody>
        <tr>
          <td>Id</td>
          <td>{props.balance && props.balance.id}</td>
        </tr>
        <tr>
          <td>Amount</td>
          <td>{props.balance && props.balance.id}</td>
        </tr>
        <tr>
          <td>Item</td>
          <td>{props.balance && props.balance.item}</td>
        </tr>
        <tr>
          <td>KindElementId</td>
          <td>{props.balance && props.balance.kind_element_id}</td>
        </tr>
        <tr>
          <td>PurposeElementId</td>
          <td>{props.balance && props.balance.purpose_element_id}</td>
        </tr>
        <tr>
          <td>PlaceElementId</td>
          <td>{props.balance && props.balance.place_element_id}</td>
        </tr>
      </tbody>
    </table >
  )
}

export { BalanceDetail };
