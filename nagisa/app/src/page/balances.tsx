import React, { useState, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useEffect } from 'react';
import { BalanceTable } from '../component/table';
import { BalanceDetail } from '../component/balanceDetail';

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
      <BalanceTable balances={balances}></BalanceTable>
    </div>
  )
}

const BalanceCreate = () => {
  const postBalance = (balance: BalanceData) => {
    axios.post('/api/v1/balance', balance).then(
    ).catch(() => {
      console.log('error');
    });
  }

  return (
    <>
      <h2>create</h2>
      <BalanceDetail />
    </>
  )
}

const BalanceEdit = () => {
  const { id } = useParams<{ id: string }>();
  const [balance, setBalance] = useState<BalanceData>();

  const getBalance = useCallback(() => {
    axios.get('/api/v1/balance/' + id).then(
      response => {
        setBalance(response.data);
      }
    ).catch(() => {
      console.log('error');
    });
  }, [id]);

  useEffect(() => {
    getBalance();
  }, [getBalance])

  return (
    <>
      <h2>edit</h2>
      <BalanceDetail balance={balance} />
    </>
  )
}

export { BalanceList, BalanceCreate, BalanceEdit };
