import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useEffect } from 'react';

type BalanceData = {
  id: number
  amount: number
  item: string
  kind_element_id: number
  purpose_element_id: number
  place_element_id: number
  date: string
}

const BalanceList = () => {
  const [balances, setBalances] = useState<BalanceData[]>([]);

  const getBalances = useCallback(() => {
    axios.get('/api/v1/balance').then(
      response => {
        setBalances(response.data);
      }
    ).catch(() => {
      console.log('error');
    });
  }, []);

  useEffect(() => {
    getBalances();
  }, [getBalances])

  return (
    <div>
      <h2>balance</h2>
      {balances.map((balance) => { return (<p key={balance.id}>{balance.id}, {balance.item}</p>) })}
    </div>
  )
}

const BalanceCreate = () => {
  return (
    <h2>create</h2>
  )
}

export { BalanceList, BalanceCreate };
