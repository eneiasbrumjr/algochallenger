<?php

use App\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        if (!User::where('username', 'admin')->first()) {
            User::create([
                'username' => 'admin',
                'type' => 'admin',
                'password' => Hash::make('123456'),
                'full_name' => 'Administrador'
            ]);
        }
    }
}
